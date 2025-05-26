import rumps
import subprocess
import shutil
import os

def find_v2raya():
    # Default to checking system PATH
    path = shutil.which("v2raya")
    if path:
        return path

    # Try common Homebrew locations manually
    common_paths = [
        "/opt/homebrew/bin/v2raya",        # Apple Silicon
        "/usr/local/bin/v2raya",           # Intel Macs
        "/opt/local/bin/v2raya",           # MacPorts (if used)
    ]

    for p in common_paths:
        if os.path.isfile(p) and os.access(p, os.X_OK):
            return p

    return None


HOME_PATH = os.path.expanduser("~")

def get_env():
    env = {
        'PATH':
                '/opt/homebrew/bin:'
                '/opt/homebrew/sbin:'
                '/usr/local/bin:'
                '/opt/local/bin:'
                '/usr/bin:'
                '/bin:'
                '/usr/sbin:'
                '/sbin:',
        'HOME': HOME_PATH, 

    }   

    return env

V2RAY_PATH = find_v2raya()
v2ray_process = None  # Global reference to the subprocess

app = rumps.App("V2RayA", menu=["Start Proxy", "Quit"], quit_button=None)


def is_running():
    return v2ray_process and v2ray_process.poll() is None


@rumps.clicked("Start Proxy")
def toggle_proxy(sender):
    global v2ray_process
    print(get_env())

    if not V2RAY_PATH or not os.path.exists(V2RAY_PATH):
        rumps.alert("Error", f"V2RayA binary not found. Please install V2RayA and ensure it's in your PATH. {V2RAY_PATH}")

    if is_running():
        # Stop the proxy
        v2ray_process.terminate()
        v2ray_process = None
        sender.title = "Start Proxy"
        # rumps.notification("V2Ray", "", "Proxy stopped.")
    else:
        try:
            # Start the proxy
            v2ray_process = subprocess.Popen([V2RAY_PATH, "--lite"],env=get_env())
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
