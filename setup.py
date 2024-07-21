import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "Chest-Cancer-Classification-Project"
AUTHOR_USER_NAME = "sat-kum"
SCR_REPO = "CNNClassifer"
AUTHOR_EMAIL = "satkum161997@gmail.com"


setuptools.setup(
    name = SCR_REPO,
    version=__version__,
    author= AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for CNN model app",
    long_description= long_description,
    long_description_content_type= "text/markdown",
    url = f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_url ={
        "Bug Tacker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"":"src"},
    packages=setuptools.find_namespace_packages(where="src")
)