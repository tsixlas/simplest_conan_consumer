from os import path
from conan import ConanFile
from conan.tools.cmake import CMakeToolchain, CMake, cmake_layout, CMakeDeps
from conan.tools.files import copy


class simplest_conanRecipe(ConanFile):
    name = "simplest_conan_consumer"
    version = "0.1"
    generators = "CMakeDeps", "CMakeToolchain"
    settings = "os", "compiler", "build_type", "arch"
    exports_sources = "CMakeLists.txt", "*.cpp", "*.h", ".so"
    package_type = "application"

    requires = [
        "simplest_conan/0.3"
    ]

    def layout(self):
        build_path = path.join("build_" + str(self.settings.arch), str(self.settings.build_type))
        self.folders.generators = build_path
        self.folders.build = build_path
        self.folders.install = build_path

    def build(self):
        self.cmake = CMake(self)
        self.cmake.configure()
        self.cmake.build()

    def package(self):
        self.cmake.install()

    def package_info(self):
        self.cpp_info.names["cmake_find_package"] = self.name
        self.cpp_info.libs = [self.name]
        self.cpp_info.system_libs.append("simplest_conan::simplest_conan")

    def generate(self):
        for dep in self.dependencies.values():
            for folder in dep.cpp_info.libdirs:
                if self.package_folder:
                    copy(self, "*.so", folder, path.join(self.package_folder, "lib"))