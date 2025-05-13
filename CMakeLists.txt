cmake_minimum_required(VERSION 3.18)
project(simplest_conan_consumer LANGUAGES CXX)

find_package(simplest_conan)

# Library
add_library(${PROJECT_NAME}_lib include/lib.h src/lib.cpp)
target_link_libraries(${PROJECT_NAME}_lib simplest_conan::simplest_conan)
target_include_directories(${PROJECT_NAME}_lib PUBLIC include)

# Executable
add_executable(${PROJECT_NAME} src/main.cpp)
target_link_libraries(${PROJECT_NAME} ${PROJECT_NAME}_lib)
install(TARGETS ${PROJECT_NAME})

#Tests
enable_testing()
find_package(GTest REQUIRED)
include(GoogleTest)

add_executable(runUnitTests test/test.cpp)
target_link_libraries(runUnitTests gtest::gtest ${PROJECT_NAME}_lib)
gtest_discover_tests(runUnitTests)