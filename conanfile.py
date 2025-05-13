from os import path
from conan import ConanFile
from conan.tools.cmake import CMake
from conan.tools.files import copy


class SimplestConanRecipe(ConanFile):
    name = "simplest_conan_consumer"
    version = "0.1"
    generators = "CMakeDeps", "CMakeToolchain"
    settings = "os", "compiler", "build_type", "arch"
    exports_sources = "CMakeLists.txt", "*.cpp", "*.h"
    package_type = "application"

    def requirements(self):
        self.requires("simplest_conan/0.3", transitive_headers=False)

        self.test_requires("gtest/1.16.0")

    def layout(self):
        build_path = path.join("build_" + str(self.settings.arch), str(self.settings.build_type))
        self.folders.generators = build_path
        self.folders.build = build_path
        self.folders.install = build_path

    def build(self):
        self.cmake = CMake(self)
        self.cmake.configure()
        self.cmake.build()
        self.cmake.test()

    def package(self):
        self.cmake.install()

    def generate(self):
        for dep in self.dependencies.values():
            for folder in dep.cpp_info.libdirs:
                if self.package_folder:
                    copy(self, "*.so", folder, path.join(self.package_folder, "lib"))