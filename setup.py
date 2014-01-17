from ez_setup import use_setuptools
use_setuptools()

from setuptools import setup, find_packages

try:
    import py2exe
except ImportError:
    pass

setup(name='digital organism simulation environment',
      version='1.0.1',
      download_url='https://github.com/mauriceling/dose/releases',
      packages=['dose', 
                'dose.copads'],
      description='Digital Organism Simulation Environment',
      long_description='''
Digital Organism Simulation Environment (DOSE)

Life is fascinating and deeply intriguing. Despite so, life forms on Earth 
or carbon-based life forms as a group is just one form, one possible sample 
of possibly a whole magnitude of life. Even then, there are many aspects of 
life that cannot be deciphered even by examining current life forms; for 
example, how did chemical reactions organize themselves into biochemical 
pathways? How did life start? How is intelligence formed?

To answer such questions, we will have to restart our evolutionary time to 
the very beginning - clearly an impossibly gargantuan task. At the same 
time, studying biological/carbon-based life forms is expensive, time 
consuming and destructive. As a molecular biologist, there is no way I can 
examine the entire genome of even a bacteria in an inanimate state, then 
somehow allow it to continue living as if time had just stopped while I 
am examining it.

However, if I can simulate a bacteria or any life form in a computer, 
then I can make a digital copy of the bacterium, pull it apart to study it 
while the original bacterium continues "living" in my virtual world without 
even knowing that it had been duplicated. Many biologists thought of virtual 
life forms as a new way to learn about life itself. Studying of virtual life 
forms is known as Artificial Life and I term "virtual life forms" as 
"digital organisms". There are several advantages in experimenting using 
digital organisms. Firstly, generation time can be much faster compared to 
most biological life. Secondly, it is usually cheaper to examine computer 
simulations than working on actual biological life. Perhaps the most 
important advantage of looking at life from this perspective is that by 
recreating life in a different medium, we are not limited to our own system 
of carbon-based life; hence, studying life as what-it-could-be.

Digital Organisms Simulation Environment (DOSE) is essentially a virtual 
world simulator for studying digital organisms. I will argue that digital 
organisms are considered living organisms (Koh and Ling, 2013). Despite so, 
being a molecular biologist by training, I have a hard time mapping 
components of digital organisms into biological life whenever such 
components are too abstract. Hence, I decided to design an artificial 
life / digital organism simulator that bears resemblance to biological 
life and ecology. 

License: Unless otherwise specified, all files in dose/copads folder will 
be licensed under Python Software Foundation License version 2; all other 
files will be GNU General Public License version 3.

Documentation can be found at http://maurice.vodien.com/project-dose

Copyright 2010-2013, Maurice HT Ling (on behalf of all authors).
''',
      author='Maurice HT Ling',
      author_email='mauriceling@acm.org',
      url='https://github.com/mauriceling/dose',
      license='GNU General Public License version 3',
      platforms=['Operating System :: OS Independent'],
      classifiers=['Development Status :: 3 - Alpha',
                   'Intended Audience :: Developers',
                   'Intended Audience :: Education',
                   'Intended Audience :: Science/Research',
                   'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
                   'Natural Language :: English',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python :: 2 :: Only',
                   'Topic :: Education',
                   'Topic :: Scientific/Engineering :: Artificial Life',
                   'Topic :: Scientific/Engineering :: Bio-Informatics',
                   'Topic :: Software Development :: Libraries :: Python Modules'
                   ],
      console=['dosecmd.py']
     )
