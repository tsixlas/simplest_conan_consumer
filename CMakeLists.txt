cmake_minimum_required(VERSION 3.18)
project(simplest_conan_consumer LANGUAGES CXX)

# Collect headers
file(GLOB src/main.cpp)

# Build the executable
add_executable(${PROJECT_NAME} src/main.cpp)

find_package(simplest_conan)
target_link_libraries(${PROJECT_NAME}
    simplest_conan::simplest_conan
)

install(TARGETS ${PROJECT_NAME} )