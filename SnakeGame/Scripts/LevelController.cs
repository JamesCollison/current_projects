using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class LevelController : MonoBehaviour
{
    public void LoadNextLevel()
    {
        Scene scene = SceneManager.GetActiveScene();
        int currentSceneIndex = scene.buildIndex;
        SceneManager.LoadScene(currentSceneIndex + 1);
    }

    public void LoadFirstLevel()
    {
        SceneManager.LoadScene(0);
    }

    public void QuitGame()
    {
        Application.Quit();
    }
}
