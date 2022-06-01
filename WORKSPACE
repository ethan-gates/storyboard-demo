load("@bazel_tools//tools/build_defs/repo:git.bzl", "git_repository")
load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")


git_repository(
    name = "build_bazel_rules_ios",
    remote = "https://github.com/bazel-ios/rules_ios.git",
    branch = "master",
)

load(
    "@build_bazel_rules_ios//rules:repositories.bzl",
    "rules_ios_dependencies"
)

rules_ios_dependencies()

load(
    "@build_bazel_rules_apple//apple:repositories.bzl",
    "apple_rules_dependencies",
)

apple_rules_dependencies()

load(
    "@build_bazel_rules_swift//swift:repositories.bzl",
    "swift_rules_dependencies",
)

swift_rules_dependencies()

load(
    "@build_bazel_apple_support//lib:repositories.bzl",
    "apple_support_dependencies",
)

apple_support_dependencies()

http_archive(
    name = "com_google_protobuf",
    strip_prefix = "protobuf-51405b6b92c2070c8edea1b44c6770e00f7027be",
    sha256 = "b50f8541baf733841121e26dad9d00abfba8766ed4d5f458bb609c26edddf812",
    url = "http://artifactory.corp.linkedin.com:8081/artifactory/ext-libraries/com/google/bazel/com_google_protobuf/51405b6b92c2070c8edea1b44c6770e00f7027be/com_google_protobuf-51405b6b92c2070c8edea1b44c6770e00f7027be.zip",
)

load(
    "@com_google_protobuf//:protobuf_deps.bzl",
    "protobuf_deps",
)

protobuf_deps()