cmake_minimum_required(VERSION 2.8)
project(mat_to_image)

set(CMAKE_CXX_STANDARD 11)
find_package(OpenCV)
include_directories(${OpenCV_INCLUDE})
message("Opencv Version:" ${OpenCV_VERSION})
add_executable(mat_to_image main.cpp)
target_link_libraries(mat_to_image ${OpenCV_LIBRARIES})
