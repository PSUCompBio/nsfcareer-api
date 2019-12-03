import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
     name='simulation',  
     version='0.1',
     scripts=['simulation'] ,
     author="vradars",
     author_email="abby@vradars.com",
     description="Utility package to generate simulation data",
     long_description=long_description,
     long_description_content_type="text/markdown",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: Yogaya License",
         "Operating System :: OS Independent",
     ],
 )
