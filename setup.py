# -*- coding: utf-8 -*-
"""
    Created on Thu Oct  2 12:05:03 2020
    
    @author: Sai chand
    """

import setuptools

with open("readme.txt", "r") as fh:
    long_description = fh.read()

setuptools.setup(
                
                 name="greendeckassi",
            
                 version="0.0.1",
                 
               
                 author="Sai chand",
                 
              
                 author_email="repalasaichand1729@gmail.com",
                 
            
                 description="Assignment of Green Deck",
                 
                 Long_description="Read en excel file throgh google drive and plot it",
                 
                 License = "MIT",
                 
                 Language = "python",
                 
                 url="https://github.com/rapchu/greendeckassi",
                 packages=setuptools.find_packages(),
                 
                 classifiers=[
                              "Programming Language :: Python :: 3",
                              "License :: OSI Approved :: MIT License",
                              "Operating System :: OS Independent",
                              ],
                 )
