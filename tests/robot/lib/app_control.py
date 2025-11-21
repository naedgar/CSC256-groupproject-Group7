import subprocess
import time
import os
import sys

try:
    import requests
except Exception:
    requests = None


class AppControl:
    """Lightweight Robot library to start and stop the Flask app used in tests.

    Keywords exposed:
    - Start App
    - Stop App
    - Wait For Server
    """

    def __init__(self):
        self.process = None

    def start_app(self, timeout: int = 30):
        """Start the Flask app as a subprocess and wait until /api/health is available.

        `timeout` is seconds to wait for the health endpoint.
        """
        if self.process and self.process.poll() is None:
            return

        python = sys.executable or "python"
        env = os.environ.copy()
        # ensure Flask doesn't use reloader in subprocess
        env.pop("PYTHONBREAKPOINT", None)

        # start the app module
        self.process = subprocess.Popen([python, "-m", "app.main"], env=env, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

        # wait for health endpoint
        self.wait_for_server(timeout)

    def stop_app(self):
        """Stop the Flask app subprocess if it was started."""
        if not self.process:
            return
        try:
            self.process.terminate()
            self.process.wait(timeout=5)
        except Exception:
            try:
                self.process.kill()
            except Exception:
                pass
        finally:
            self.process = None

    def wait_for_server(self, timeout: int = 30):
        """Poll `/api/health` until it returns 200 or `timeout` seconds elapse."""
        url = os.environ.get("TEST_BASE_URL", "http://127.0.0.1:5000") + "/api/health"
        end = time.time() + int(timeout)
        while time.time() < end:
            try:
                if requests is not None:
                    r = requests.get(url, timeout=2)
                    if r.status_code == 200:
                        return
            except Exception:
                pass
            time.sleep(0.5)
        raise RuntimeError(f"Server at {url} did not respond with 200 within {timeout}s")
