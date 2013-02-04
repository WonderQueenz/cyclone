# coding: utf-8
#
# Copyright 2010 Alexandre Fiori
# based on the original Tornado by Facebook
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

__author__ = "Alexandre Fiori"
__version__ = version = "git-2013011801"

git://github.com/fiorix/cyclone.git

#include <stdio.h>
 #include <core.h>
 using Core;
 int main(int argc, string_t ? args)
 {
    if (argc <= 1) {
       printf("Usage: hello-cyclone <name>\n");
       return 1;
    }
    printf("Hello from Cyclone, %s\n", args[1]);
    return 0;

