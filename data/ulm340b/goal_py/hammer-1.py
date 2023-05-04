
    # Steps:
    #  1. Put gripper near the nail
    #  2. Lift the hammer
    #  3. Swing the hammer downward to hit the nail
    # To hit the nail with the hammer, we need to put the robot's gripper near
    # the nail.
    if check("the robot's gripper is not near the nail"):
        robot.move_gripper("near the nail", close_gripper=True)
    # Once the gripper is near the nail, we need to pull the hammer away from
    # the nail to swing it.
    if check("the robot's gripper is not above the nail and the robot's gripper is not below the nail"):
        robot.move_gripper("above the nail")
    # Once the hammer is not near the nail, we can swing the hammer downward to
    # hit the nail.
    if check("the robot's gripper is not near the nail"):
        robot.move_gripper("near the nail")
[eod] [code]from setuptools import setup


setup(
    name='django-sentry',
    version='1.2.2',
    author='Simon de Haan',
    author_email='simon@praekelt.org',
    packages=[
        'sentry',
        'sentry.auth',
        'sentry.forms',
        'sentry.templatetags',
        'sentry.management',
        'sentry.management.commands',
        'sentry.migrations',
    ],
    include_package_data=True,
    license='BSD License',
    description='Sentry integration for Django.',
    long_description=open('README.rst', 'r').read(),
    install_requires=[
        'Django >= 1.4.2',
    ],
    url='https://github.com/getsentry/sentry-django',
    classifiers=[
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'Topic :: Software Development',
        'Topic :: Software Development :: Build Tools',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Software Development :: Libraries :: Python Modules'