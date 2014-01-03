<?php
    if (isset($_SERVER['SCRIPT_FILENAME'])) {
    $timestamp = filemtime(__FILE__);
    header('Last-Modified: ' . $timestamp);
    $expires = 60*60*24*14;
    header("Pragma: public");
    header("Cache-Control: maxage=".$expires);
    header('Expires: ' . gmdate('D, d M Y H:i:s', time()+$expires) . ' GMT');
    header('Vary: Accept-Encoding');
    $pathinfo = pathinfo($_SERVER['SCRIPT_FILENAME']);
    $extension = $pathinfo['extension'];
    if ($extension == 'css') {
		header('Content-type: text/css; charset=utf-8');
		header("Expires: ".gmdate("D, d M Y H:i:s", time() + $offset)." GMT");
		header('Vary: Accept Encoding');
    }
    if ($extension == 'js') {
		header('Content-type: text/javascript; charset=utf-8');
		header("Expires: ".gmdate("D, d M Y H:i:s", time() + $offset)." GMT");
		header('Vary: Accept Encoding');
    }
    }?>
