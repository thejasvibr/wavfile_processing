# -*- coding: utf-8 -*-
"""Extracts single channels from wav files and names them serially
as single WAV files  
Created on Tue May 29 16:35:19 2018

@author: tbeleyur
"""
import re 
import sys 
sys.path.append('C://Users//tbeleyur//Documents//common//Python_common//audio_video_pairing')
sys.path.append('C://Users//tbeleyur//Documents//common//Python_common//')
sys.path.append('C://Users//tbeleyur//Documents//common//Python_common//python_fieldrecorder//')
import easygui as eg 
import ADC_delay 


file_dir = eg.fileopenbox()
rec_folder = re.search('(.*)MULTIWAV', file_dir).group(1)
fs, multich = ADC_delay.read_wavfile(file_dir)
five_channels = ADC_delay.select_channels([0,1,2,34,5,6,7],multich)
file_timestamp =  str(re.search('MULTIWAV_(.*)', file_dir).group(1))
ADC_delay.save_as_singlewav_timestamped(five_channels,fs,rec_folder+'Mic',
                          file_timestamp= file_timestamp)