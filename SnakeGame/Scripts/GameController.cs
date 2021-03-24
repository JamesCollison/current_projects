using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class GameController : MonoBehaviour
{
    [SerializeField] [Range(11, 50)] float gameSpeed = 1f;
    [SerializeField] float difficultyMod = 0.2f;
    [SerializeField] GameObject gameOverScreen;

    Vector2 nextMove;
    float snakeSpeed;
    bool playing = true;
    float score = 0;
    float stage = 1;
    int level = 1;

    InputController inputManager;
    TextManager textManager;
    Snake snake;

    private void Awake()
    {
        MakeSingleton();
    }

    void Start()
    {
        SetSnakeSpeed();
        SetInputManager();
        SetTextManager();
        SetText();
        SetGameOverScreen(false);
    }

    void Update()
    {
        nextMove = inputManager.GetInput();
    }

    private void MakeSingleton()
    {
        GameController[] nControllers = FindObjectsOfType<GameController>();
        if (nControllers.Length > 1) { Destroy(gameObject); }
        else { DontDestroyOnLoad(gameObject); }
    }

    public void GameOver()
    {
        playing = false;
    }

    public bool IsPlaying()
    {
        return playing;
    }

    public void IncreaseLevel()
    {
        level++;
        SetText();
    }

    public void IncreaseScore(float value)
    {
        score += value;
    }

    public void IncreaseStage(float value)
    {
        var increase = value * difficultyMod;
        gameSpeed += increase;
        SetSnakeSpeed();
    }

    void SetSnakeSpeed()
    {
        snakeSpeed = 1 / gameSpeed;
    }

    void SetInputManager()
    {
        inputManager = FindObjectOfType<InputController>();
    }

    void SetTextManager()
    {
        textManager = FindObjectOfType<TextManager>();
    }

    public void SetGameOverScreen(bool state)
    {
        gameOverScreen.SetActive(state);
    }

    public void SetText()
    {
        textManager.setScoreText((int)score);
        textManager.setLevelText(level);
        textManager.setStageText((int)gameSpeed - 10);
    }

    public Vector2 GetNextMove()
    {
        inputManager.MoveExecuted();
        return nextMove;
    }

    public float GetSnakeSpeed()
    {
        return snakeSpeed;
    }

    public void Restart()
    {
        Destroy(gameObject);
    }
}
