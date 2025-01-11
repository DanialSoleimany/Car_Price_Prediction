#!/usr/bin/env python
# coding: utf-8

styles = """
<style>
    .styled-div {
        background: #D473D4; 
        color: #ffffff; 
        border-radius: 50px; 
        padding: 10px 15px; 
        font-size: 18px; 
        font-weight: bold; 
        text-align: center; 
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; 
        margin-bottom: 20px;
    }
    
    .nav-link {
        display: inline-block; 
        background-color: #9b4dfa; 
        color: white; 
        padding: 5px 10px; 
        text-align: center; 
        text-decoration: none; 
        border-radius: 5px; 
        font-family: 'Arial', sans-serif; 
        font-size: 10px; 
        float: left;
    }
</style>
"""

get_ipython().run_line_magic('store', 'styles')
