[Docker for Windows]: https://docs.docker.com/docker-for-windows/install/ "Download Docker for Windows"

# Windows Setup

## Required

- Requirements listed in the [README](../README.md)
- [Docker for Windows]
- Windows 10 Pro with Hyper-V enabled<sup>1</sup>
- Make<sup>2</sup>

## Setup

__After [Docker for Windows] installation__:

1. Right click the small docker icon in the system tray
2. Choose settings
3. Choose Shared Drives
4. Click your C drive (or whatever drive your project is on)
5. Click Apply
6. Enter your credentials (if prompted)

__Login to Dockerhub__:

```bash
cd path/to/your/project
docker login
```

---

- <small><sup>1</sup> Otherwise you will need to use docker-toolbox and another virtualization software like VMWare Fusion</small>
- <small><sup>2</sup> You must have make installed on Windows, and ensure that you have an alias in your powershell profile that points to the proper make.exe.*</small>
