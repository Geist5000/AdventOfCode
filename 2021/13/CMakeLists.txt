cmake_minimum_required(VERSION 3.16)
project(13)

set(CMAKE_CXX_STANDARD 14)

add_executable(13
        first.c)

target_sources(13 PRIVATE data.txt)

