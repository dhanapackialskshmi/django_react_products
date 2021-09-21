import React from 'react'
import {Link} from 'react-router-dom'


export default function Nav() {
    return (
        <div>
             <nav className='nav justify-content-center'>
                <Link className='nav-link' to='/list'>Product List</Link>
                <Link className='nav-link' to='/product'>Add Products</Link>

            </nav>
        </div>
    )
}


