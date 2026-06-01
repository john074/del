#[test]
fn test_split_path_root() {
    let (dir, file) = split_path("/test.txt").unwrap();
    assert_eq!(dir, "/");
    assert_eq!(file, "test.txt");
}

#[test]
fn test_to_short_name_basic() {
    let short = to_short_name("test.txt");
    let expected = b"TEST TXT";
    assert_eq!(&short[0..3], &expected[0..3]);

    let short2 = to_short_name("bootloader.bin");
    let expected2 = b"BOOTLOADBIN";
    assert_eq!(&short2[0..11], &expected2);
}

#[test]
fn test_ata_device_new() {
    let dev = AtaDevice::new(0x1F0, 0x3F6, 0);
    assert_eq!(dev.io_base, 0x1F0);
    assert_eq!(dev.control_base, 0x3F6);
    assert_eq!(dev.drive, 0);
}

#[test]
fn test_ata_device_drive_selection() {
    let master = AtaDevice::new(0x1F0, 0x3F6, 0);
    let slave = AtaDevice::new(0x1F0, 0x3F6);
    assert_eq!(master.drive, 0);
    assert_eq!(slave.drive, 1);
}
