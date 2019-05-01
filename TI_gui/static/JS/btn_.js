function show(){
	var file;
	for(var i=0; i<document.getElementById("file").files.length; i++){
		file = document.getElementById("file").files[i];
		alert(file.name);
	}
	return file.name
}