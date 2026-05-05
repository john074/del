#[unsafe(no_mangle)]
pub extern "C" fn _start() {
    TEST::std::mkdir("my_dir");
    exit();
}
