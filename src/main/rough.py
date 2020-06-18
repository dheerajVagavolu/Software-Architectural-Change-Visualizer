from file_map_engine.ast_engine import make_ast


test_path = 'test\python\examples\\custom_object.py'
code = open(test_path, 'r').read()

tree = make_ast(code)

print(tree.keys())


# 


function getdiff(a, b){
      var added = 0;
      var deleted = 0;

      var key;
      var key2;
      var key3;
      var key4;

      for (key in a){
        if(a.hasOwnProperty(key)){
          run = 1;
          val = a[key]['value']
          for (key2 in b){
              if(b.hasOwnProperty(key2)){
              val2 = b[key2]['value']
              if(val == val2){
                run = 0;
              }
            }
          }
          if(run == 1){
            added = added + 1;
          }
        }
      }


      for (key3 in b){
        if(b.hasOwnProperty(key3)){
          run = 1;
          val = b[key3]['value']
          for (key4 in a){
            if(a.hasOwnProperty(key4)){
              val2 = a[key4]['value']
              if(val == val2){
                run = 0;
              }
            }
          }
          if(run == 1){
            deleted = deleted + 1;
          }
        }
      }


    return [added, deleted]

}

function set_diff(a, b){
  document.getElementById('num_added').innerHTML = 'Added: ' + a;
  document.getElementById('num_deleted').innerHTML = 'Removed: ' + b; 
}
function set_diff1(a){
  document.getElementById('num_added').innerHTML = 'Added: ' + a;
  document.getElementById('num_deleted').innerHTML = 'Removed: 0'; 
}

        #   // console.log(temp_new_dat);

        #   // for(var i in temp_new_dat){
        #   //   from = key;
        #   //   to = temp_new_dat[i][0];

        #   //   type_ = temp_new_dat[i][1];
        #   //   // alert(type_);
        #   //   console.log(from + " : " + to);


            
        #   //   temp_node_dir = {id: from, normal: {
        #   //       height: 6,
        #   //       fill: '#F4D03F',
        #   //   }, hovered: {
        #   //     height: 8,
        #   //       fill: '#F4D03F'
        #   //   }, selected: {
        #   //     height: 10,
        #   //       fill: '#F4D03F'
        #   //   }, shape: "square"}

        #   //   new_data2['nodes'].push(temp_node_dir);


            

        #   //   if(type_ == "funcDef"){

        #   //     temp_node_dir2 = {id: to, normal: {
        #   //             height: 8,
        #   //             fill: '#2C3E50',
        #   //         }, hovered: {
        #   //           height: 10,
        #   //             fill: '#2C3E50'
        #   //         }, selected: {
        #   //           height: 12,
        #   //             fill: '#2C3E50'
        #   //         }, shape: "square"}

        #   //         new_data2['nodes'].push(temp_node_dir2);
        #   //     }

        #   //     if(type_ == "ClassDef"){

        #   //         temp_node_dir2 = {id: to, normal: {
        #   //                 height: 8,
        #   //                 fill: '#633974',
        #   //             }, hovered: {
        #   //               height: 10,
        #   //                 fill: '#633974'
        #   //             }, selected: {
        #   //               height: 12,
        #   //                 fill: '#633974'
        #   //             }, shape: "circle"}

        #   //             new_data2['nodes'].push(temp_node_dir2);
        #   //         }

        #   //     if(type_ == "func"){

        #   //     temp_node_dir2 = {id: to, normal: {
        #   //             height: 6,
        #   //             fill: '#76D7C4',
        #   //         }, hovered: {
        #   //           height: 8,
        #   //             fill: '#76D7C4'
        #   //         }, selected: {
        #   //           height: 10,
        #   //             fill: '#76D7C4'
        #   //         }, shape: "square"}

        #   //         new_data2['nodes'].push(temp_node_dir2);
        #   //     }

        #   //     if(type_ == "module"){

        #   //       temp_node_dir2 = {id: to, normal: {
        #   //               height: 3,
        #   //               fill: '#2980B9',
        #   //           }, hovered: {
        #   //             height: 4,
        #   //               fill: '#2980B9'
        #   //           }, selected: {
        #   //             height: 5,
        #   //               fill: '#2980B9'
        #   //           }, shape: "square"}

        #   //           new_data2['nodes'].push(temp_node_dir2);
        #   //       }

        #   //       if(type_ == "file"){

        #   //         temp_node_dir2 = {id: to, normal: {
        #   //                 height: 3,
        #   //                 fill: '#7B7D7D',
        #   //             }, hovered: {
        #   //               height: 4,
        #   //                 fill: '#7B7D7D'
        #   //             }, selected: {
        #   //               height: 5,
        #   //                 fill: '#7B7D7D'
        #   //             }, shape: "square"}

        #   //             new_data2['nodes'].push(temp_node_dir2);
        #   //         }






        #   //   temp_edge_dir = {'from': from, 'to':to}
        #   //   new_data2['edges'].push(temp_edge_dir);


        #   