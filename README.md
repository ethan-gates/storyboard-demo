# storyboard-demo

Demonstrating an issue where a StoryboardLink action is attempted twice and errors out

`ERROR: /Users/egates/Documents/code/demo/BUILD.bazel:22:16: for demo-intermediates/storyboards/demo, previous action: action 'StoryboardLink demo-intermediates/storyboards/demo', attempted action: action 'StoryboardLink demo-intermediates/storyboards/demo'`

To reproduce run `bazel build demo`

Looking at the expanded macros in the output of `bazel query //:all --output build`, it appears as if the Main.storyboard file is used by the launch_screen_storyboard_name filegroup which is odd considering there is no launch storyboard at all.  The bazel query output can be seen in `bazel_query_all.py`.
