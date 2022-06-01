# /Users/egates/Documents/code/demo/BUILD.bazel:8:15
config_setting(
  name = "Debug",
  values = {"compilation_mode": "dbg"},
)
# Rule Debug instantiated at (most recent call last):
#   /Users/egates/Documents/code/demo/BUILD.bazel:8:15 in <toplevel>

# /Users/egates/Documents/code/demo/BUILD.bazel:15:15
config_setting(
  name = "Release",
  values = {"compilation_mode": "opt"},
)
# Rule Release instantiated at (most recent call last):
#   /Users/egates/Documents/code/demo/BUILD.bazel:15:15 in <toplevel>

# /Users/egates/Documents/code/demo/BUILD.bazel:22:16
ios_application(
  name = "demo",
  visibility = ["//visibility:public"],
  generator_name = "demo",
  generator_function = "ios_application",
  generator_location = "/Users/egates/Documents/code/demo/BUILD.bazel:22:16",
  bundle_id = "com.linkedin.demo",
  infoplists = ["//:demo/Info.plist"],
  minimum_os_version = "13.0",
  families = ["iphone", "ipad"],
  deps = ["//:demo.dep_middleman", "//:demo.force_load_direct_deps"],
  launch_storyboard = "//:demo_launch_screen_storyboard",
  frameworks = ["//:demo.framework_middleman"],
)
# Rule demo instantiated at (most recent call last):
#   /Users/egates/Documents/code/demo/BUILD.bazel:22:16                                                                in <toplevel>
#   /private/var/tmp/_bazel_egates/1849ab92d76d94c6b49af70eaeb55f8a/external/build_bazel_rules_ios/rules/app.bzl:76:32 in ios_application
# Rule ios_application defined at (most recent call last):
#   /private/var/tmp/_bazel_egates/1849ab92d76d94c6b49af70eaeb55f8a/external/build_bazel_rules_apple/apple/internal/ios_rules.bzl:1993:58    in <toplevel>
#   /private/var/tmp/_bazel_egates/1849ab92d76d94c6b49af70eaeb55f8a/external/build_bazel_rules_apple/apple/internal/rule_factory.bzl:1213:16 in _create_apple_bundling_rule

# /Users/egates/Documents/code/demo/BUILD.bazel:22:16
dep_middleman(
  name = "demo.dep_middleman",
  tags = ["manual"],
  generator_name = "demo",
  generator_function = "ios_application",
  generator_location = "/Users/egates/Documents/code/demo/BUILD.bazel:22:16",
  deps = ["//:demo_swift", "//:demo_objc", "//:demo_private_headers"],
)
# Rule demo.dep_middleman instantiated at (most recent call last):
#   /Users/egates/Documents/code/demo/BUILD.bazel:22:16                                                                in <toplevel>
#   /private/var/tmp/_bazel_egates/1849ab92d76d94c6b49af70eaeb55f8a/external/build_bazel_rules_ios/rules/app.bzl:73:18 in ios_application
# Rule dep_middleman defined at (most recent call last):
#   /private/var/tmp/_bazel_egates/1849ab92d76d94c6b49af70eaeb55f8a/external/build_bazel_rules_ios/rules/internal/framework_middleman.bzl:204:21 in <toplevel>

# /Users/egates/Documents/code/demo/BUILD.bazel:22:16
force_load_direct_deps(
  name = "demo.force_load_direct_deps",
  tags = ["manual"],
  generator_name = "demo",
  generator_function = "ios_application",
  generator_location = "/Users/egates/Documents/code/demo/BUILD.bazel:22:16",
  deps = ["//:demo_swift", "//:demo_objc", "//:demo_private_headers"],
)
# Rule demo.force_load_direct_deps instantiated at (most recent call last):
#   /Users/egates/Documents/code/demo/BUILD.bazel:22:16                                                                in <toplevel>
#   /private/var/tmp/_bazel_egates/1849ab92d76d94c6b49af70eaeb55f8a/external/build_bazel_rules_ios/rules/app.bzl:65:27 in ios_application
# Rule force_load_direct_deps defined at (most recent call last):
#   /private/var/tmp/_bazel_egates/1849ab92d76d94c6b49af70eaeb55f8a/external/build_bazel_rules_ios/rules/force_load_direct_deps.bzl:28:30 in <toplevel>

# /Users/egates/Documents/code/demo/BUILD.bazel:22:16
framework_middleman(
  name = "demo.framework_middleman",
  tags = ["manual"],
  generator_name = "demo",
  generator_function = "ios_application",
  generator_location = "/Users/egates/Documents/code/demo/BUILD.bazel:22:16",
  framework_deps = ["//:demo_swift", "//:demo_objc", "//:demo_private_headers"],
)
# Rule demo.framework_middleman instantiated at (most recent call last):
#   /Users/egates/Documents/code/demo/BUILD.bazel:22:16                                                                in <toplevel>
#   /private/var/tmp/_bazel_egates/1849ab92d76d94c6b49af70eaeb55f8a/external/build_bazel_rules_ios/rules/app.bzl:69:24 in ios_application
# Rule framework_middleman defined at (most recent call last):
#   /private/var/tmp/_bazel_egates/1849ab92d76d94c6b49af70eaeb55f8a/external/build_bazel_rules_ios/rules/internal/framework_middleman.bzl:99:27 in <toplevel>

# /Users/egates/Documents/code/demo/BUILD.bazel:22:16
resources_filegroup(
  name = "demo_data",
  generator_name = "demo",
  generator_function = "ios_application",
  generator_location = "/Users/egates/Documents/code/demo/BUILD.bazel:22:16",
  srcs = ["//:Resources/**/*.storyboard", "//:Resources/**/*.xcassets"],
  extensions_to_filter = ["xcdatamodeld", "xcdatamodel", "xcmappingmodel", "xcassets", "xcstickers"],
)
# Rule demo_data instantiated at (most recent call last):
#   /Users/egates/Documents/code/demo/BUILD.bazel:22:16                                                                              in <toplevel>
#   /private/var/tmp/_bazel_egates/1849ab92d76d94c6b49af70eaeb55f8a/external/build_bazel_rules_ios/rules/app.bzl:58:28               in ios_application
#   /private/var/tmp/_bazel_egates/1849ab92d76d94c6b49af70eaeb55f8a/external/build_bazel_rules_ios/rules/library.bzl:843:63          in apple_library
#   /private/var/tmp/_bazel_egates/1849ab92d76d94c6b49af70eaeb55f8a/external/build_bazel_rules_ios/rules/library/resources.bzl:62:24 in wrap_resources_in_filegroup
# Rule resources_filegroup defined at (most recent call last):
#   /private/var/tmp/_bazel_egates/1849ab92d76d94c6b49af70eaeb55f8a/external/build_bazel_rules_ios/rules/library/resources.bzl:41:27 in <toplevel>

# /Users/egates/Documents/code/demo/BUILD.bazel:22:16
filegroup(
  name = "demo_launch_screen_storyboard",
  tags = ["manual"],
  generator_name = "demo",
  generator_function = "ios_application",
  generator_location = "/Users/egates/Documents/code/demo/BUILD.bazel:22:16",
  srcs = ["//:demo_data"],
  output_group = "launch_screen_storyboard",
)
# Rule demo_launch_screen_storyboard instantiated at (most recent call last):
#   /Users/egates/Documents/code/demo/BUILD.bazel:22:16                                                                      in <toplevel>
#   /private/var/tmp/_bazel_egates/1849ab92d76d94c6b49af70eaeb55f8a/external/build_bazel_rules_ios/rules/app.bzl:58:28       in ios_application
#   /private/var/tmp/_bazel_egates/1849ab92d76d94c6b49af70eaeb55f8a/external/build_bazel_rules_ios/rules/library.bzl:1010:21 in apple_library

# /Users/egates/Documents/code/demo/BUILD.bazel:22:16
objc_library(
  name = "demo_objc",
  tags = ["manual"],
  generator_name = "demo",
  generator_function = "ios_application",
  generator_location = "/Users/egates/Documents/code/demo/BUILD.bazel:22:16",
  data = [],
  srcs = [],
  non_arc_srcs = [],
  pch = "@build_bazel_rules_ios//rules/library:common.pch",
  deps = ["//:demo_public_hmap", "//:demo_private_hmap", "//:demo_private_angled_hmap", "//:demo_swift_doublequote_hmap", "//:demo_swift_angle_bracket_hmap", "//:demo_swift"] + select({"@build_bazel_rules_ios//:virtualize_frameworks": ["//:demo_swift_vfs", "//:demo_vfs"], "//conditions:default": []}),
  defines = [],
  hdrs = [],
  sdk_includes = [],
  sdk_frameworks = [],
  weak_sdk_frameworks = [],
  sdk_dylibs = [],
  copts = [] + [] + select({"@build_bazel_rules_ios//:virtualize_frameworks": ["-ivfsoverlay$(execpath :demo_vfs)", "-F/build_bazel_rules_ios/frameworks"], "//conditions:default": []}) + ["-I$(execpath :demo_private_hmap)", "-I$(execpath :demo_public_hmap)", "-I$(execpath :demo_private_angled_hmap)", "-iquote$(execpath :demo_private_hmap)", "-fmodules", "-fmodule-name=demo", "-iquote$(execpath :demo_swift_doublequote_hmap)", "-I$(execpath :demo_swift_angle_bracket_hmap)", "-I."] + select({"@build_bazel_rules_ios//:use_global_index_store": ["-index-store-path", "bazel-out/rules_ios_global_index_store.indexstore"], "//conditions:default": ["-index-store-path", "$(GENDIR)//rules_ios_objc_library_demo_objc.indexstore"]}),
)
# Rule demo_objc instantiated at (most recent call last):
#   /Users/egates/Documents/code/demo/BUILD.bazel:22:16                                                                     in <toplevel>
#   /private/var/tmp/_bazel_egates/1849ab92d76d94c6b49af70eaeb55f8a/external/build_bazel_rules_ios/rules/app.bzl:58:28      in ios_application
#   /private/var/tmp/_bazel_egates/1849ab92d76d94c6b49af70eaeb55f8a/external/build_bazel_rules_ios/rules/library.bzl:991:24 in apple_library
# Rule objc_library defined at (most recent call last):
#   /virtual_builtins_bzl/common/objc/objc_library.bzl:153:20 in <toplevel>

# /Users/egates/Documents/code/demo/BUILD.bazel:22:16
filegroup(
  name = "demo_private_angled_hdrs",
  tags = ["manual"],
  generator_name = "demo",
  generator_function = "ios_application",
  generator_location = "/Users/egates/Documents/code/demo/BUILD.bazel:22:16",
  srcs = [],
)
# Rule demo_private_angled_hdrs instantiated at (most recent call last):
#   /Users/egates/Documents/code/demo/BUILD.bazel:22:16                                                                     in <toplevel>
#   /private/var/tmp/_bazel_egates/1849ab92d76d94c6b49af70eaeb55f8a/external/build_bazel_rules_ios/rules/app.bzl:58:28      in ios_application
#   /private/var/tmp/_bazel_egates/1849ab92d76d94c6b49af70eaeb55f8a/external/build_bazel_rules_ios/rules/library.bzl:800:21 in apple_library

# /Users/egates/Documents/code/demo/BUILD.bazel:22:16
headermap(
  name = "demo_private_angled_hmap",
  tags = ["manual"],
  generator_name = "demo",
  generator_function = "ios_application",
  generator_location = "/Users/egates/Documents/code/demo/BUILD.bazel:22:16",
  namespace = "demo",
  hdrs = ["//:demo_private_angled_hdrs"],
)
# Rule demo_private_angled_hmap instantiated at (most recent call last):
#   /Users/egates/Documents/code/demo/BUILD.bazel:22:16                                                                     in <toplevel>
#   /private/var/tmp/_bazel_egates/1849ab92d76d94c6b49af70eaeb55f8a/external/build_bazel_rules_ios/rules/app.bzl:58:28      in ios_application
#   /private/var/tmp/_bazel_egates/1849ab92d76d94c6b49af70eaeb55f8a/external/build_bazel_rules_ios/rules/library.bzl:812:14 in apple_library
# Rule headermap defined at (most recent call last):
#   /private/var/tmp/_bazel_egates/1849ab92d76d94c6b49af70eaeb55f8a/external/build_bazel_rules_ios/rules/hmap.bzl:94:17 in <toplevel>

# /Users/egates/Documents/code/demo/BUILD.bazel:22:16
filegroup(
  name = "demo_private_hdrs",
  tags = ["manual"],
  generator_name = "demo",
  generator_function = "ios_application",
  generator_location = "/Users/egates/Documents/code/demo/BUILD.bazel:22:16",
  srcs = [],
)
# Rule demo_private_hdrs instantiated at (most recent call last):
#   /Users/egates/Documents/code/demo/BUILD.bazel:22:16                                                                     in <toplevel>
#   /private/var/tmp/_bazel_egates/1849ab92d76d94c6b49af70eaeb55f8a/external/build_bazel_rules_ios/rules/app.bzl:58:28      in ios_application
#   /private/var/tmp/_bazel_egates/1849ab92d76d94c6b49af70eaeb55f8a/external/build_bazel_rules_ios/rules/library.bzl:795:21 in apple_library

# /Users/egates/Documents/code/demo/BUILD.bazel:22:16
_private_headers(
  name = "demo_private_headers",
  tags = ["manual"],
  generator_name = "demo",
  generator_function = "ios_application",
  generator_location = "/Users/egates/Documents/code/demo/BUILD.bazel:22:16",
  headers = [],
)
# Rule demo_private_headers instantiated at (most recent call last):
#   /Users/egates/Documents/code/demo/BUILD.bazel:22:16                                                                      in <toplevel>
#   /private/var/tmp/_bazel_egates/1849ab92d76d94c6b49af70eaeb55f8a/external/build_bazel_rules_ios/rules/app.bzl:58:28       in ios_application
#   /private/var/tmp/_bazel_egates/1849ab92d76d94c6b49af70eaeb55f8a/external/build_bazel_rules_ios/rules/library.bzl:1021:25 in apple_library
# Rule _private_headers defined at (most recent call last):
#   /private/var/tmp/_bazel_egates/1849ab92d76d94c6b49af70eaeb55f8a/external/build_bazel_rules_ios/rules/library.bzl:38:24 in <toplevel>

# /Users/egates/Documents/code/demo/BUILD.bazel:22:16
headermap(
  name = "demo_private_hmap",
  tags = ["manual"],
  generator_name = "demo",
  generator_function = "ios_application",
  generator_location = "/Users/egates/Documents/code/demo/BUILD.bazel:22:16",
  hdrs = ["//:demo_private_hdrs"],
)
# Rule demo_private_hmap instantiated at (most recent call last):
#   /Users/egates/Documents/code/demo/BUILD.bazel:22:16                                                                     in <toplevel>
#   /private/var/tmp/_bazel_egates/1849ab92d76d94c6b49af70eaeb55f8a/external/build_bazel_rules_ios/rules/app.bzl:58:28      in ios_application
#   /private/var/tmp/_bazel_egates/1849ab92d76d94c6b49af70eaeb55f8a/external/build_bazel_rules_ios/rules/library.bzl:806:14 in apple_library
# Rule headermap defined at (most recent call last):
#   /private/var/tmp/_bazel_egates/1849ab92d76d94c6b49af70eaeb55f8a/external/build_bazel_rules_ios/rules/hmap.bzl:94:17 in <toplevel>

# /Users/egates/Documents/code/demo/BUILD.bazel:22:16
filegroup(
  name = "demo_public_hdrs",
  tags = ["manual"],
  generator_name = "demo",
  generator_function = "ios_application",
  generator_location = "/Users/egates/Documents/code/demo/BUILD.bazel:22:16",
  srcs = [],
)
# Rule demo_public_hdrs instantiated at (most recent call last):
#   /Users/egates/Documents/code/demo/BUILD.bazel:22:16                                                                     in <toplevel>
#   /private/var/tmp/_bazel_egates/1849ab92d76d94c6b49af70eaeb55f8a/external/build_bazel_rules_ios/rules/app.bzl:58:28      in ios_application
#   /private/var/tmp/_bazel_egates/1849ab92d76d94c6b49af70eaeb55f8a/external/build_bazel_rules_ios/rules/library.bzl:773:21 in apple_library

# /Users/egates/Documents/code/demo/BUILD.bazel:22:16
headermap(
  name = "demo_public_hmap",
  tags = ["manual"],
  generator_name = "demo",
  generator_function = "ios_application",
  generator_location = "/Users/egates/Documents/code/demo/BUILD.bazel:22:16",
  namespace = "demo",
  hdrs = ["//:demo_public_hdrs"],
)
# Rule demo_public_hmap instantiated at (most recent call last):
#   /Users/egates/Documents/code/demo/BUILD.bazel:22:16                                                                     in <toplevel>
#   /private/var/tmp/_bazel_egates/1849ab92d76d94c6b49af70eaeb55f8a/external/build_bazel_rules_ios/rules/app.bzl:58:28      in ios_application
#   /private/var/tmp/_bazel_egates/1849ab92d76d94c6b49af70eaeb55f8a/external/build_bazel_rules_ios/rules/library.bzl:782:14 in apple_library
# Rule headermap defined at (most recent call last):
#   /private/var/tmp/_bazel_egates/1849ab92d76d94c6b49af70eaeb55f8a/external/build_bazel_rules_ios/rules/hmap.bzl:94:17 in <toplevel>

# /Users/egates/Documents/code/demo/BUILD.bazel:22:16
swift_library(
  name = "demo_swift",
  tags = ["manual"],
  generator_name = "demo",
  generator_function = "ios_application",
  generator_location = "/Users/egates/Documents/code/demo/BUILD.bazel:22:16",
  features = ["swift.no_generated_module_map"] + select({"@build_bazel_rules_ios//:virtualize_frameworks": ["swift.vfsoverlay"], "//conditions:default": []}),
  data = ["//:demo_data"],
  deps = ["//:demo_public_hmap", "//:demo_private_hmap", "//:demo_private_angled_hmap"] + select({"@build_bazel_rules_ios//:virtualize_frameworks": ["//:demo_swift_vfs"], "//conditions:default": []}),
  srcs = ["//:demo/Sources/AppDelegate.swift", "//:demo/Sources/SceneDelegate.swift", "//:demo/Sources/ViewController.swift"],
  copts = [] + [] + select({"@build_bazel_rules_ios//:virtualize_frameworks": ["-Xfrontend", "-vfsoverlay$(execpath :demo_swift_vfs)", "-Xfrontend", "-F/build_bazel_rules_ios/frameworks", "-I/build_bazel_rules_ios/frameworks", "-Xcc", "-ivfsoverlay$(execpath :demo_swift_vfs)", "-Xcc", "-F/build_bazel_rules_ios/frameworks"], "//conditions:default": []}) + ["-Xcc", "-I$(execpath :demo_private_hmap)", "-Xcc", "-I$(execpath :demo_public_hmap)", "-Xcc", "-I$(execpath :demo_private_angled_hmap)", "-Xcc", "-iquote$(execpath :demo_private_hmap)", "-Xcc", "-D__SWIFTC__", "-Xfrontend", "-no-clang-module-breadcrumbs", "-Xcc", "-I."],
  defines = [],
  module_name = "demo",
  swiftc_inputs = [],
  generated_header_name = "demo-Swift.h",
  generates_header = True,
)
# Rule demo_swift instantiated at (most recent call last):
#   /Users/egates/Documents/code/demo/BUILD.bazel:22:16                                                                     in <toplevel>
#   /private/var/tmp/_bazel_egates/1849ab92d76d94c6b49af70eaeb55f8a/external/build_bazel_rules_ios/rules/app.bzl:58:28      in ios_application
#   /private/var/tmp/_bazel_egates/1849ab92d76d94c6b49af70eaeb55f8a/external/build_bazel_rules_ios/rules/library.bzl:892:22 in apple_library
# Rule swift_library defined at (most recent call last):
#   /private/var/tmp/_bazel_egates/1849ab92d76d94c6b49af70eaeb55f8a/external/build_bazel_rules_swift/swift/internal/swift_library.bzl:276:21 in <toplevel>

# /Users/egates/Documents/code/demo/BUILD.bazel:22:16
headermap(
  name = "demo_swift_angle_bracket_hmap",
  tags = ["manual"],
  generator_name = "demo",
  generator_function = "ios_application",
  generator_location = "/Users/egates/Documents/code/demo/BUILD.bazel:22:16",
  testonly = False,
  namespace = "demo",
  hdrs = [],
  direct_hdr_providers = ["//:demo_swift"],
)
# Rule demo_swift_angle_bracket_hmap instantiated at (most recent call last):
#   /Users/egates/Documents/code/demo/BUILD.bazel:22:16                                                                     in <toplevel>
#   /private/var/tmp/_bazel_egates/1849ab92d76d94c6b49af70eaeb55f8a/external/build_bazel_rules_ios/rules/app.bzl:58:28      in ios_application
#   /private/var/tmp/_bazel_egates/1849ab92d76d94c6b49af70eaeb55f8a/external/build_bazel_rules_ios/rules/library.bzl:935:18 in apple_library
# Rule headermap defined at (most recent call last):
#   /private/var/tmp/_bazel_egates/1849ab92d76d94c6b49af70eaeb55f8a/external/build_bazel_rules_ios/rules/hmap.bzl:94:17 in <toplevel>

# /Users/egates/Documents/code/demo/BUILD.bazel:22:16
headermap(
  name = "demo_swift_doublequote_hmap",
  tags = ["manual"],
  generator_name = "demo",
  generator_function = "ios_application",
  generator_location = "/Users/egates/Documents/code/demo/BUILD.bazel:22:16",
  testonly = False,
  namespace = "demo",
  hdrs = [],
  direct_hdr_providers = ["//:demo_swift"],
)
# Rule demo_swift_doublequote_hmap instantiated at (most recent call last):
#   /Users/egates/Documents/code/demo/BUILD.bazel:22:16                                                                     in <toplevel>
#   /private/var/tmp/_bazel_egates/1849ab92d76d94c6b49af70eaeb55f8a/external/build_bazel_rules_ios/rules/app.bzl:58:28      in ios_application
#   /private/var/tmp/_bazel_egates/1849ab92d76d94c6b49af70eaeb55f8a/external/build_bazel_rules_ios/rules/library.bzl:922:18 in apple_library
# Rule headermap defined at (most recent call last):
#   /private/var/tmp/_bazel_egates/1849ab92d76d94c6b49af70eaeb55f8a/external/build_bazel_rules_ios/rules/hmap.bzl:94:17 in <toplevel>

# /Users/egates/Documents/code/demo/BUILD.bazel:22:16
framework_vfs_overlay(
  name = "demo_swift_vfs",
  tags = ["manual"],
  generator_name = "demo",
  generator_function = "ios_application",
  generator_location = "/Users/egates/Documents/code/demo/BUILD.bazel:22:16",
  testonly = False,
  framework_name = "demo",
  has_swift = True,
  hdrs = [],
  private_hdrs = [],
  deps = [],
)
# Rule demo_swift_vfs instantiated at (most recent call last):
#   /Users/egates/Documents/code/demo/BUILD.bazel:22:16                                                                     in <toplevel>
#   /private/var/tmp/_bazel_egates/1849ab92d76d94c6b49af70eaeb55f8a/external/build_bazel_rules_ios/rules/app.bzl:58:28      in ios_application
#   /private/var/tmp/_bazel_egates/1849ab92d76d94c6b49af70eaeb55f8a/external/build_bazel_rules_ios/rules/library.bzl:741:26 in apple_library
# Rule framework_vfs_overlay defined at (most recent call last):
#   /private/var/tmp/_bazel_egates/1849ab92d76d94c6b49af70eaeb55f8a/external/build_bazel_rules_ios/rules/framework/vfs_overlay.bzl:412:29 in <toplevel>

# /Users/egates/Documents/code/demo/BUILD.bazel:22:16
framework_vfs_overlay(
  name = "demo_vfs",
  tags = ["manual"],
  generator_name = "demo",
  generator_function = "ios_application",
  generator_location = "/Users/egates/Documents/code/demo/BUILD.bazel:22:16",
  testonly = False,
  framework_name = "demo",
  has_swift = True,
  hdrs = [],
  private_hdrs = [],
  deps = ["//:demo_public_hmap", "//:demo_private_hmap", "//:demo_private_angled_hmap"],
)
# Rule demo_vfs instantiated at (most recent call last):
#   /Users/egates/Documents/code/demo/BUILD.bazel:22:16                                                                     in <toplevel>
#   /private/var/tmp/_bazel_egates/1849ab92d76d94c6b49af70eaeb55f8a/external/build_bazel_rules_ios/rules/app.bzl:58:28      in ios_application
#   /private/var/tmp/_bazel_egates/1849ab92d76d94c6b49af70eaeb55f8a/external/build_bazel_rules_ios/rules/library.bzl:878:26 in apple_library
# Rule framework_vfs_overlay defined at (most recent call last):
#   /private/var/tmp/_bazel_egates/1849ab92d76d94c6b49af70eaeb55f8a/external/build_bazel_rules_ios/rules/framework/vfs_overlay.bzl:412:29 in <toplevel>

