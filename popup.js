var images = document.getElementsByTagName('img'); 
var srcList = [];
var req_imgs = [];
var fake = [];
for(var i = 0; i < images.length; i++) {
	if(images[i].width > 100 && images[i].height > 100 && (images[i].src).match(/\.(jpeg|jpg|png)$/) != null){
		srcList.push(images[i].src);
		req_imgs.push(images[i]);
		fake.push(0);
	}
}
console.log(srcList)
for (var i in srcList){
	var link = srcList[i];
	var data = {img_url: link, indx: i};
	window.fetch("https://0.0.0.0:4201/img", {method: 'POST', body: JSON.stringify(data),
		headers: {'Content-Type': 'application/json'}}).then(res => res.json()).then(res => {
			console.log(srcList[res.indx] + '\t' + res.result)
			if(!res.result){
				req_imgs[res.indx].style.opacity=.3;
			}
		});
}