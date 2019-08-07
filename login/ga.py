#!/usr/bin/env python
# coding:utf8
 
"""
结合 Google Authenticator App 使用
其中使用pyotp模块是最简单和方便的实现
"""
 
import pyotp
 
def main():
    gtoken = 'my google token' # google token value
    t = pyotp.TOTP(gtoken)
    print t.now() 
 
if __name__ =='__main__':
    main()
 
