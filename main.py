import rumps
import subprocess
import shutil
import os

V2RAY_PATH = shutil.which("v2raya")


v2ray_process = None  # Global reference to the subprocess

app = rumps.App("V2RayA", menu=["Start Proxy", "Quit"], quit_button=None)


def is_running():
    return v2ray_process and v2ray_process.poll() is None


@rumps.clicked("Start Proxy")
def toggle_proxy(sender):
    global v2ray_process

    if not V2RAY_PATH or not os.path.exists(V2RAY_PATH):
        rumps.alert("Error", "V2RayA binary not found. Please install V2RayA and ensure it's in your PATH.")



    if is_running():
        # Stop the proxy
        v2ray_process.terminate()
        v2ray_process = None
        sender.title = "Start Proxy"
        # rumps.notification("V2Ray", "", "Proxy stopped.")
    else:
        try:
            # Start the proxy
            v2ray_process = subprocess.Popen([V2RAY_PATH, "--lite"])
            sender.title = "Stop Proxy"
            # rumps.notification("V2Ray", "", "Proxy started.")
        except Exception as e:
            rumps.alert(f"Failed to start proxy:\n{str(e)}")


@rumps.clicked("Quit")
def quit_app(_):
    global v2ray_process
    if is_running():
        v2ray_process.terminate()
    rumps.quit_application()


app.run()
