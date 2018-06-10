(function() {
	var video = document.getElementById('video'),
	canvas = document.getElementById('canvas'),
	context = canvas.getContext('2d'),
	vendorUrl = window.URL || window.webkitURL;
	navigator.getMedia = navigator.getUserMedia || 
			     navigator.webkitGetUserMedia || 
			     navigator.mozGetUserMedia || 
			     navigator.msGetUserMedia;

	navigator.getMedia({
			video:true,
			audio:false
			}, function(stream){
			   video.src = vendorUrl.createObjectURL(stream);
video.play();
			}, function(error){
			   //Error Handling
			});
var face_name = document.getElementById('face-name').value;

document.getElementById('capture').addEventListener('click',function(){
context.drawImage(video,0,0,400,300);
photo.setAttribute('src',canvas.toDataURL("image/jpg"));
face_image.setAttribute('href',canvas.toDataURL("image/jpg"));
});
})();

function onClick(){
var face_name = document.getElementById('face-name').value;

};
