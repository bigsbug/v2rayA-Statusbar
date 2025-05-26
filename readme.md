# V2RayA macOS Menu Bar Controller

A simple macOS menu bar application that allows you to start and stop the V2RayA proxy server using a convenient GUI. This app uses [rumps](https://github.com/jaredks/rumps) for menu bar integration and `py2app` for packaging.

---

## Features

- Start and stop the V2RayA proxy with one click.
- Displays notifications when proxy is started or stopped.
- Clean and minimal menu bar interface.
- Built as a native `.app` for macOS.

---

##  Requirements

- macOS (tested on Monterey and newer)
- **Python 3.7** (Recommended for best compatibility with `py2app`)
- [V2RayA](http://v2raya.org/) must be installed and available in your `$PATH`

## How To Use

- Install required libraries:

    ```bash
    pip install -r requirements.txt
    ```

- Build the macOS application:

    ```bash
    python setup.py py2app
    ```

- After building, you'll find your app inside the `dist` folder as:

    ```
    dist/V2rayA.app
    ```

- You can move this `.app` to your `/Applications` folder and launch it like any native macOS application.
