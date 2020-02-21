# Impressive Uploader

[![Open Issues](https://img.shields.io/github/issues/nightwarrior-xxx/social?style=for-the-badge&logo=github)](https://github.com/nightwarriorftw/ImpressiveUploader/issues) [![Forks](https://img.shields.io/github/forks/nightwarrior-xxx/social?style=for-the-badge&logo=github)](https://github.com/nightwarriorftw/ImpressiveUploader/network/members) [![Stars](https://img.shields.io/github/stars/nightwarrior-xxx/social?style=for-the-badge&logo=reverbnation)](https://github.com/nightwarriorftw/ImpressiveUploader/stargazers) ![Made with Python](https://img.shields.io/badge/Made%20with-Python-blueviolet?style=for-the-badge&logo=python) ![Open Source Love](https://img.shields.io/badge/Open%20Source-%E2%99%A5-red?style=for-the-badge&logo=open-source-initiative) ![Built with Love](https://img.shields.io/badge/Built%20With-%E2%99%A5-critical?style=for-the-badge&logo=ko-fi) [![Follow Me](https://img.shields.io/twitter/follow/nightwarriorftw?color=blue&label=Follow%20%40nightwarriorftw&logo=twitter&style=for-the-badge)](https://twitter.com/intent/follow?screen_name=nightwarriorftw) [![Telegram](https://img.shields.io/badge/Telegram-Chat-informational?style=for-the-badge&logo=telegram)](https://telegram.me/nightwarriorftw)

## :ledger: Index

- [About](#beginner-about)
- [Usage](#zap-usage)
- [Developmen Environment](#nut_and_bolt-development-environment)
- [File Structure](#file_folder-file-structure)
- [Community](#cherry_blossom-community)
  - [Contribution](#fire-contribution)
  - [Branches](#cactus-branches)
  - [Guideline](#exclamation-guideline)
- [Gallery](#camera-gallery)
- [Credit/Acknowledgment](#star2-creditacknowledgment)
- [License](#lock-license)

## :beginner: About

Uploading large files to server is a tough task and with specially if doesn't support a stop and continue feature. Impressive uploader overcomes this problem and provide you a solution where you can upload large files and stop it.

## :zap: Usage
The solution also packaged on docker image and now it can be deployed directly to the kubernetes.

### :nut_and_bolt: Development Environment

#### 1. Clone the Repository

```Bash
git clone https://github.com/nightwarrior-xxx/social.git
cd social
```

#### 2. Install the dependencies

Install docker, docker-compose


#### 6. Run the application:

```BASH
docker-compose up
```

### :file_folder: File Structure

```
├── db.sqlite3
├── django
├── docker-compose.yml
├── dockerfile
├── impressiveUploader
│   ├── __init__.py
│   ├── __init__.pyc
│   ├── __pycache__
│   │   ├── __init__.cpython-37.pyc
│   │   ├── __init__.cpython-38.pyc
│   │   ├── settings.cpython-37.pyc
│   │   ├── settings.cpython-38.pyc
│   │   ├── urls.cpython-37.pyc
│   │   ├── urls.cpython-38.pyc
│   │   ├── wsgi.cpython-37.pyc
│   │   └── wsgi.cpython-38.pyc
│   ├── settings.py
│   ├── settings.pyc
│   ├── urls.py
│   ├── urls.pyc
│   └── wsgi.py
├── LICENSE
├── manage.py
├── requirements.txt
├── static
│   ├── css
│   ├── img
│   │   ├── cancel.png
│   │   └── resume.png
│   └── js
│       ├── progressBar.js
│       └── upload.js
├── static_cdn
│   └── media_root
│       ├── Instant Family HD Rip.mkv
│       └── TheGreatHack.mkv
└── uploader
    ├── admin.py
    ├── admin.pyc
    ├── api
    │   ├── __pycache__
    │   │   ├── serializers.cpython-37.pyc
    │   │   ├── serializers.cpython-38.pyc
    │   │   ├── urls.cpython-37.pyc
    │   │   ├── urls.cpython-38.pyc
    │   │   ├── views.cpython-37.pyc
    │   │   └── views.cpython-38.pyc
    │   ├── serializers.py
    │   ├── urls.py
    │   └── views.py
    ├── apps.py
    ├── forms.py
    ├── __init__.py
    ├── __init__.pyc
    ├── migrations
    │   ├── 0001_initial.py
    │   ├── __init__.py
    │   └── __pycache__
    │       ├── 0001_initial.cpython-37.pyc
    │       ├── 0001_initial.cpython-38.pyc
    │       ├── __init__.cpython-37.pyc
    │       └── __init__.cpython-38.pyc
    ├── models.py
    ├── models.pyc
    ├── __pycache__
    │   ├── admin.cpython-37.pyc
    │   ├── admin.cpython-38.pyc
    │   ├── forms.cpython-37.pyc
    │   ├── forms.cpython-38.pyc
    │   ├── __init__.cpython-37.pyc
    │   ├── __init__.cpython-38.pyc
    │   ├── models.cpython-37.pyc
    │   ├── models.cpython-38.pyc
    │   ├── urls.cpython-37.pyc
    │   ├── urls.cpython-38.pyc
    │   ├── utils.cpython-37.pyc
    │   ├── utils.cpython-38.pyc
    │   ├── views.cpython-37.pyc
    │   └── views.cpython-38.pyc
    ├── templates
    │   └── upload.html
    ├── tests.py
    ├── urls.py
    ├── utils.py
    └── views.py
```

## :cherry_blossom: Community

### :fire: Contribution

Your contributions are always welcome and appreciated. Following are the things you can do to contribute to this project.

1.  **Report a bug** <br>
    If you think you have encountered a bug, and I should know about it, feel free to report by making an issue and I will take care of it.

2.  **Request a feature** <br>
    You can also request for a feature. Just make an issue, and if it will viable, it will be picked for development.

3.  **Create a pull request** <br>
    It can't get better then this, your pull request will be appreciated.

### :cactus: Branches

I use an agile continuous integration methodology, so the version is frequently updated and development is really fast.

1. **`dev`** is the development branch.

2. **`master`** is the production branch.

**Steps to work with feature branch**

1. To start working on a new feature, create a new branch prefixed with `FEATURE` and followed by feature name. (ie. `FEATURE-<feature name>`)
2. Once you are done with your changes, you can raise PR.

**Steps to create a pull request**

1. Make a PR to `dev` branch.
2. Comply with the best practices and guidelines e.g. where the PR concerns visual elements it should have an image showing the effect.

After this, changes will be merged.

### :exclamation: Guideline

Make sure that there is onle one extra line after the file ends and remember the indentation.

## :camera: Gallery

Pictures of project.

## :star2: Credit/Acknowledgment

Credits goes to me and other contributors

## :lock: License

[LICENSE](/LICENSE)