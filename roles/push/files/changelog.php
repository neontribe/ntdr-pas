<?php

$lines = file(__DIR__ . '/changelog.txt');

$new = array();
$new[] = trim($lines[0]);
$new[] = trim($lines[1]);
$new[] = "";

$searchpath = __DIR__ . '/sites';

$directory = new RecursiveDirectoryIterator( $searchpath, RecursiveDirectoryIterator::KEY_AS_FILENAME | RecursiveDirectoryIterator::CURRENT_AS_FILEINFO);
$files = new RegexIterator( new RecursiveIteratorIterator($directory), '#^changelog\.txt$#', RegexIterator::MATCH, RegexIterator::USE_KEY);

foreach ($files as $file) {
    $filename = $file->getPathname();
    if (file_exists($filename)) {
        $_lines = file($filename);
        if (strpos($_lines[1], '===') === 0) {
            // $new[] = basename(dirname($filename)) . ': ' . $_lines[0];
            $new[] = sprintf("%15.15s\t%-30.30s", basename(dirname($filename)), trim($_lines[0]));
        }
        elseif (strpos($lines[1], '+--') === 0) {
            // $new[] = basename(dirname($filename)) . ': ' . $_lines[0];
            $new[] = sprintf("%15.15s\t%-30.30s", basename(dirname($filename)), trim($_lines[0]));
        }
    }
}

$date = $lines[1];
$parts = explode(' ', $lines[0]);
$version = $parts[1];
$lock = __DIR__ . '/.' . $version . '.lock';
if (!file_exists($lock)) {
  exec('rm *.lock');
  array_shift($lines);
  array_shift($lines);
  $fh = fopen('changelog.txt', 'w');
  foreach ($new as $line) {
    fwrite($fh, $line . "\n");
  }
  fwrite($fh, '--------------');
  foreach ($lines as $line) {
    fwrite($fh, trim($line) . "\n");
  }
  fclose($fh);

  // file_put_contents($lock, array());

  echo "Changelog updated\n";
}
else {
  echo "Skipping\n";
}
