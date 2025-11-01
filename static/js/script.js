// التحكم بالقائمة الجانبية
function toggleMenu() {
    const menu = document.getElementById("sideMenu");
    menu.style.right = (menu.style.right === "0px") ? "-250px" : "0px";
}

// التحكم في القائمة المنسدلة للدخول
function toggleLoginMenu() {
    const menu = document.getElementById("loginMenu");
    menu.style.display = (menu.style.display === "flex") ? "none" : "flex";
}

// عرض الأقسام أو نبذة الجامعة
function showSection(id) {
    const sections = document.querySelectorAll("section");
    sections.forEach(sec => sec.classList.remove("active"));
    document.getElementById(id).classList.add("active");
    document.getElementById("sideMenu").style.right = "-250px";
}
