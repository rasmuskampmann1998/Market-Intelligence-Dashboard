import asyncio
from asyncio import subprocess
import logging
import platform
from crawl4ai import AsyncWebCrawler
from urllib.parse import urljoin, urlparse
from typing import Set, List
from loguru import logger
import psutil

logger.add("app.log", level="INFO") 

class Crawl4AINewsScraper:
    def __init__(self, max_pages: int = 7, max_depth: int = 2, delay: float = 0.2):
        self.max_pages = max_pages
        self.max_depth = max_depth
        self.delay = delay
        self.processes_to_kill = []

    async def scrape(self, url: str) -> str:
        visited: Set[str] = set()
        content_list: List[str] = []
        crawler = AsyncWebCrawler()

        try:
            await crawler.__aenter__()

            async def crawl_recursive(current_url: str, depth: int):
                if depth > self.max_depth or current_url in visited or len(visited) >= self.max_pages:
                    return

                visited.add(current_url)
                try:
                    result = await crawler.arun(current_url)
                    if result.success and result.markdown:
                        content_list.append(result.markdown)
                except Exception as e:
                    logger.warning(f"Failed to scrape {current_url}: {e}")
                await asyncio.sleep(self.delay)

                links = result.links.get("internal", []) if result else []
                for link in links:
                    if len(visited) >= self.max_pages:
                        break
                    href = link.get("href") if isinstance(link, dict) else link
                    if href:
                        full_url = urljoin(current_url, href)
                        if urlparse(full_url).netloc == urlparse(url).netloc:
                            await crawl_recursive(full_url, depth + 1)

            await crawl_recursive(url, 0)

        finally:
            try:
                await crawler.__aexit__(None, None, None)
                logger.info("Closed crawler instance cleanly")
            except Exception as e:
                logger.error(f"Error closing crawler: {e}")

            self.kill_zombie_browsers()

        logger.info(f"Scraped {len(visited)} pages from {url}")
        return "\n\n".join(content_list)

    def start_browser(self):
        if platform.system() == "Windows":
            proc = subprocess.Popen(['chrome', '--headless', '--remote-debugging-port=9222'])
        else:
            proc = subprocess.Popen(['google-chrome', '--headless', '--remote-debugging-port=9222'])
        self.processes_to_kill.append(proc.pid)
        return proc

    def kill_zombie_browsers(self):
        try:
            for pid in self.processes_to_kill:
                try:
                    process = psutil.Process(pid)
                    process.terminate()  # Gracefully terminate
                    process.wait(timeout=5)
                    logger.info(f"Killed browser process with PID {pid}")
                except psutil.NoSuchProcess:
                    logger.warning(f"Process {pid} is no longer running.")
                except Exception as e:
                    logger.warning(f"Failed to kill process {pid}: {e}")
        except Exception as e:
            logger.warning(f"Failed to kill browser processes: {e}")
