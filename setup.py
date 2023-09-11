from setuptools import setup, find_packages


def get_requirements(file_path):
    '''
    this fubction will the list of requirements'''
    requirements  = []

    with open(file_path, 'r') as f:
        requirements  = f.readlines()
        requirements = [req.replace('/n','') for req in requirements]
    return requirements 



setup(

        name="project2",
        version='0.0.1',
        author="nasirhussain",
        author_email="aghanhussain@gmail.com",
        packages=find_packages(),
        install_require = get_requirements('requirements.txt')
    )