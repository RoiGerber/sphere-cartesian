import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# פונקציה למציאת נקודת ההקרנה על הכדור
def project_to_sphere(x, y, z_surface=-1):
    # קו עובר דרך (x, y, z_surface) ל-(0, 0, 1)
    # נדרוש שהנקודה על הקו תהיה במרחק 1 ממרכז הכדור
    A = x**2 + y**2 + (z_surface - 1)**2
    t = 1 / np.sqrt(A)  # פתרון t כך שהמרחק מנקודת ההקרנה למרכז הכדור יהיה 1
    
    # נקודת ההקרנה על הכדור
    x_proj = t * x
    y_proj = t * y
    z_proj = z_surface + t * (1 - z_surface)
    
    return x_proj, y_proj, z_proj

# פונקציה לקבלת קו מוקרן לפי פונקציה מתמטית
def plot_projected_function(f, x_range):
    # נבחר טווח x לשרטוט
    x_vals = np.linspace(*x_range, 100)
    y_vals = f(x_vals)  # חישוב ערכי הפונקציה
    
    # הקרנת כל נקודה על הכדור
    x_proj_vals = []
    y_proj_vals = []
    z_proj_vals = []
    
    for x, y in zip(x_vals, y_vals):
        x_proj, y_proj, z_proj = project_to_sphere(x, y)
        x_proj_vals.append(x_proj)
        y_proj_vals.append(y_proj)
        z_proj_vals.append(z_proj)
    
    return np.array(x_proj_vals), np.array(y_proj_vals), np.array(z_proj_vals)

# פונקציה מתמטית לדוגמה: f(x) = 7x + 13
def linear_function(x):
    return 0.5 * x  # פונקציה לינארית מתונה יותר, כדי להמחיש טוב יותר

# הגדרת מערכת הצירים והתמורה ל-3D
def plot_white_sphere_with_function_projection():
    # הגדרת טווח הערכים של U ו-V עבור קואורדינטות כדוריות
    u_vals = np.linspace(0, 2 * np.pi, 100)
    v_vals = np.linspace(0, np.pi, 100)
    
    # יצירת רשת של נקודות עבור הכדור
    U, V = np.meshgrid(u_vals, v_vals)
    X = np.sin(V) * np.cos(U)
    Y = np.sin(V) * np.sin(U)
    Z = np.cos(V)
    
    # יצירת גרף
    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(111, projection='3d')
    
    # שרטוט פני הכדור בצבע לבן עם שקיפות גבוהה (alpha = 0.9)
    ax.plot_wireframe(X, Y, Z, color='gray', rstride=5, cstride=5)

    # שרטוט הקו המוקרן על פני הכדור לפי הפונקציה
    x_proj_vals, y_proj_vals, z_proj_vals = plot_projected_function(linear_function, x_range=(-2, 2))
    ax.plot(x_proj_vals, y_proj_vals, z_proj_vals, color='orange', linewidth=4)

    # הגדרות עבור תצוגה נוחה
    ax.set_box_aspect([1, 1, 1])  # שמירה על פרופורציות שוות לכל הצירים
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    # שינוי זווית הצפייה כדי לראות את הקו בבירור
    ax.view_init(elev=30, azim=60)

    # הגדלת טווח צירים כדי להבטיח שהכל ברור
    ax.set_xlim([-2, 2])
    ax.set_ylim([-2, 2])
    ax.set_zlim([-2, 2])
    
    # הצגת הכדור עם הקו המוקרן
    plt.show()

# קריאה לפונקציה כדי לשרטט את הכדור הלבן עם הקו המוקרן
plot_white_sphere_with_function_projection()
