function multiplyMatrices(matrix1, matrix2){
            if (matrix1.length <= 0){
                return false
            }else if(matrix2.length <= 0){
                return false
            }else if(matrix1[0].length != matrix2.length){
                return false
            }

            output = []
            // Iterate every row in matrix1
            for (row_index = 0; row_index < matrix1.length; row_index++){
                output.push([])
                // Iterate over every col in matrix2
                for (col_index = 0; col_index < matrix2[0].length; col_index++){
                    output_num = 0
                    // Iterate over every no. in matrix1[row_index] and get corresponding no. in col_index of matrix2
                    for (num_index = 0; num_index < matrix1[row_index].length; num_index++){
                        output_num += matrix1[row_index][num_index] * matrix2[num_index][col_index]
                    }
                    output[row_index].push(output_num)
                }
            } return output

        }