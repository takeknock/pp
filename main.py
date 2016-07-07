# -*- coding: utf-8 -*-
"""
Created on Thu Jul  7 18:58:16 2016

@author: takeknock
"""

from pandas import DataFrame
import pandas as pd
import xml.etree.ElementTree as ET


if __name__ == "__main__":
    """
        同じcountryの情報でyearを上書きする。
        上書きしたxmlを別ファイルで出力する。
    """

    tree = ET.parse('D:/40_workspace/07_Python/pp/sample.xml')
    root_dest = tree.getroot()

    tree_source = ET.parse('D:/40_workspace/07_Python/pp/sample2.xml')
    root_source = tree_source.getroot()

    # print(root_source.tag, root_source.attrib)

    target = 'Liechtenstein'
    year = 0

    for child_source in root_source:
        if child_source.attrib['name'] == target:
            year = child_source.find('year').text
            data = {'year': [year]}
    year_frame = DataFrame(data, index=[target])
    print(year_frame['year'][target])
    """
    for child_source in root_source:
        # print(child_source.tag, child_source.attrib)
        for child_dest in root_dest:
            if child_dest.attrib['name'] == target:
                if child_source.attrib['name'] == target:
                    tst = child_source.find('year').text
                    print(child_dest.find('year').text)
                    print(tst)
                    child_dest.find('year').text
    """
    """
    for year in root_dest.iter('year'):
        print(year.text)
    """

    for country in root_dest.findall('country'):
        if country.attrib['name'] == target:
            country.find('year').text = year_frame['year'][target]
            print(country.find('year').text)

    tree.write('D:/40_workspace/07_Python/pp/output.xml')
