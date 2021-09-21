import React, { useContext } from 'react'
import {UserContext} from '../Context/userContext'


export default function List() {
    const {price}=useContext(UserContext)
    return (
        <div>
            <h2>ProductList</h2>
            {price}
        </div>
    )
}
