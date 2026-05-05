#[unsafe(no_mangle)]
pub extern "C" fn _start() {
    TEST::std::mkdir("my_dir");
    exit();
}

#[unsafe(no_mangle)]
pub extern "C" fn _start() {
    let mut task = multitasking::Task::new(subproc(), Some(5));
    syscall::spawn_task((&mut task as *mut multitasking::Task) as u64);
    exit();
}

async fn subproc() {
    for i in 0..15 {
        println!("A");
        sleep(2000).await;
    }
    exit();
}
