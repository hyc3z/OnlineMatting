cmake_minimum_required(VERSION 3.13)
project(AlphaMatting)

set(CMAKE_CXX_STANDARD 14)

include_directories(.)
find_package(OpenCV REQUIRED)
add_executable(AlphaMatting
        main.cpp
        SharedMatting.cpp
        SharedMatting.h)
