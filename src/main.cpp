#include <iostream>
#include <simplest_conan/simplest_conan.h>
#include "lib.h"

int main() {
    SimpleClass simpleClass;
    hello_world_helper("Hi!");
    if (testSuccess(true)==true) {
        std::cout << "Hello successful World!" << std::endl;
    }
}
