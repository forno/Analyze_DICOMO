cmake_minimum_required(VERSION 3.10.3)
project(decomo_night_session)

set(CMAKE_CXX_STANDARD          17  CACHE STRING "CXX standard version")
set(CMAKE_CXX_STANDARD_REQUIRED ON  CACHE BOOL   "version required")
set(CMAKE_CXX_EXTENSIONS        OFF CACHE BOOL   "compiler extension")

add_executable(create_human_vector src/create_human_vector.cpp)
