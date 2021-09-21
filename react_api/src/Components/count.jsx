import React,{useContext} from 'react'
import {ProductContext} from '../Context/userContext'

export default function Count() {
    // const[product,setProduct]=useState([])
   
    // useEffect(()=>{
    //     setProduct(['Canon','Camera',500])
    // },[])
    
    // const[products]= useContext(ProductContext)
    // console.log(products)
    
    return (
        <div>
            <h2>Total Products:</h2>
         {/* <h2>{products.length}</h2> */}
        </div>
    )
}
