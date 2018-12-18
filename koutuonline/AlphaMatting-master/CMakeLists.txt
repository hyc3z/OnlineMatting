cmake_minimum_required(VERSION 3.12)
project(AlphaMatting_master)

set(CMAKE_CXX_STANDARD 14)

include_directories(.)
find_package(OpenCV REQUIRED)
message(STATUS "OpenCV library status:")
message(STATUS "    version: ${OpenCV_VERSION}")
message(STATUS "    libraries: ${OpenCV_LIBS}")
message(STATUS "    include paths: ${OpenCV_INCLUDE_DIRS}")


add_executable(main main.cpp)
target_link_libraries(main ${OpenCV_LIBS})
