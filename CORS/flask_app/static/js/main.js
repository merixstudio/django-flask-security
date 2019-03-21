function getMusic(){
    $.get('http://localhost:8000/api/v1/albums/', (data)=>{
        var albumList = $('#album-list');
        data.forEach((element) => {
            albumList.append(element.title +' by ' + element.artist.name + '<br/><ul>');
            element.songs.forEach((song) => {
                albumList.append('<li>' + song.title + '</li>');
            });
            albumList.append('</ul><hr>');
        });
    });
}
