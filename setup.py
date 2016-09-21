from setuptools import setup, find_packages

setup(name='worldclock',
      version='0.1',
      packages=find_packages(),
      url='https://github.com/hypestar/world-clock-curse',
      license='http://opensource.org/licenses/MIT',
      classifiers=(
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License ',
          'Natural Language :: English',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3.4',
      ),
      keywords='curses clock commandline cli',
      entry_points = {
        'console_scripts' : ['worldclock = worldclock:run']
      }
)
