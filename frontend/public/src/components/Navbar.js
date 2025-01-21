import React from 'react';
import { Link } from 'react-router-dom';

const Navbar = () => {
    return (
        <nav style={styles.navbar}>
            <div style={styles.logo}>AIris AI</div>
            <ul style={styles.navLinks}>
                <li style={styles.navItem}>
                    <Link to="/" style={styles.navLink}>Home</Link>
                </li>
                <li style={styles.navItem}>
                    <Link to="/features" style={styles.navLink}>Features</Link>
                </li>
                <li style={styles.navItem}>
                    <Link to="/about" style={styles.navLink}>About</Link>
                </li>
                <li style={styles.navItem}>
                    <Link to="/contact" style={styles.navLink}>Contact</Link>
                </li>
            </ul>
        </nav>
    );
};

const styles = {
    navbar: {
        display: 'flex',
        justifyContent: 'space-between',
        alignItems: 'center',
        backgroundColor: '#282c34',
        padding: '10px 20px',
        color: '#fff',
    },
    logo: {
        fontSize: '1.5em',
        fontWeight: 'bold',
    },
    navLinks: {
        display: 'flex',
        listStyle: 'none',
        margin: 0,
        padding: 0,
    },
    navItem: {
        margin: '0 10px',
    },
    navLink: {
        color: '#61dafb',
        textDecoration: 'none',
        fontSize: '1em',
    },
};

export default Navbar;
