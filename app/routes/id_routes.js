//routes/id_routes.js

module.exports = function(app,db){
    app.post('/ids',(req,res)=>{
        const id = req.body;
        db.collection('ids').insert(id,(err,result)=>{
          if(err){
            res.send({'error': 'An error has occurred','raw error message':err})
          }else {
            res.send(result.ops[0]);
          }
        });
    });
    app.get('/ids',(req,res)=>{
        db.collection('ids').find({},(err,item) =>{
            if (err) {
                res.send({'error': 'An error has occurred'});
            }
            else{
                res.send(item)
            }
        });
    });
}
